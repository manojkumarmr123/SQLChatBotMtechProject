import os
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_chroma import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI

from few_shots import few_shots

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env (especially Google api key)

os.environ["LANGSMITH_TRACING_V2"] = "true"
os.environ["LANGSMITH_API_KEY"] = "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"
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
def get_few_shot_db_chain():
    llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=os.environ["GOOGLE_API_KEY"])

    db_user = "manoj"
    db_password = "571422"
    db_host = "localhost"
    db_name = "classicmodels"

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.environ["GOOGLE_API_KEY"])
    to_vectorize = [" ".join(example.values()) for example in few_shots]
    vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=few_shots)
    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vectorstore,
        k=2,
    )

    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer", ],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=_mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"],  # These variables are used in the prefix and suffix
    )

    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt)
    return chain

if __name__ == "__main__":
    chain = get_few_shot_db_chain()
    print(chain.run("List all customers in France with a credit limit over 40000"))


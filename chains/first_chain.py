from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

from config.openai_conf import OPEN_AI_KEY


def llm_predict():
    llm = OpenAI(openai_api_key=OPEN_AI_KEY)
    chat_model = ChatOpenAI(openai_api_key=OPEN_AI_KEY)
    text = "What would be a good company name for a company that makes colorful socks?"
    messages = [HumanMessage(content=text)]

    # print("=============== predict ================\n")
    # llm_rsp = llm.predict(text)
    # print("llm predict rsp: \n" + llm_rsp)
    # char_rsp = chat_model.predict(text)
    # print("chat predict rsp: \n" + char_rsp)

    print("=============== predict message ================\n")
    llm_rsp = llm.predict_messages(messages)
    print("llm predict message rsp: \n" + str(llm_rsp))
    chat_rsp = chat_model.predict_messages(messages)
    print("chat predict message rsp: \n" + str(chat_rsp))


def llm_template():
    pass

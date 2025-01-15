import streamlit as st
import google.generativeai as genai

# Gemini API 키 설정
GOOGLE_API_KEY = "AIzaSyD4ltnPGEDXXu1A77oVU54QCgdyXM4NBR4"
genai.configure(api_key=GOOGLE_API_KEY)

# 모델 설정
model = genai.GenerativeModel('gemini-pro')

def init_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def main():
    st.title("IT 기술 챗봇 🤖")
    
    init_session_state()

    # 채팅 히스토리 표시
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 사용자 입력
    if prompt := st.chat_input("IT 관련 질문을 해주세요"):
        # 사용자 메시지 추가
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Gemini API 응답 생성
        response = model.generate_content(prompt)
        
        # 챗봇 응답 표시
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})

if __name__ == "__main__":
    main()

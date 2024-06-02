import streamlit as st

# 예시코드 
# import streamlit as st
import plotly.express as px

df = px.data.gapminder()

if 'final_dataframe' not in st.session_state:
  # session state 에 final 이라는 값이 없으면, 
  st.session_state['final_dataframe']= df
  # 초기 값 설정 : session_state에 final_dataframe키 값에 초기값 데이터를 집어넣습니다 .

#아래 코드는 df의 테이블 값이 바뀌더라도 interactive하게 연동되서 바뀌지 않습니다
st.table(df)

#  아래 코드는  이제 dataframe가 조작될 때 마다 session_state객체 안에 final_dataframe값을 변경하면, 
#  수정 될 때  계속 바뀌어서 보여줍니다. 
st.table(st.session_state.final_dataframe)


# ----------------------------------
# st.session_state.key = 'value2'     # Attribute API
# st.session_state['key'] = 'value3'  # Dictionary like API 

# st.write(st.session_state)
# # st.write(st.session_state['value'])

# With magic:
st.session_state
 
# # Initialization
# if 'key' not in st.session_state:
#     st.session_state['key'] = 'value'

# # Session State also supports attribute based syntax
# if 'key' not in st.session_state:
#     st.session_state.key = 'value' 
    
# # Read
# st.write(st.session_state.key)


# if 'user_input' not in st.session_state:
#     st.session_state['user_input'] = ''
 
# user_input = st.text_input("텍스트를 입력하세요")
# if user_input:
#     st.session_state['user_input'] = user_input
 
# st.write(f"입력한 내용: {st.session_state['user_input']}")

# if 'user_inputs' not in st.session_state:
#     st.session_state['user_inputs'] = []
 
# user_input = st.text_input("Enter some text")
# if user_input:
#     st.session_state['user_inputs'].append(user_input)
 
# st.write(f"You entered: {st.session_state['user_inputs']}")
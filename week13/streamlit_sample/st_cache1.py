import streamlit as st
import numpy as np
import time

# Caching = 어떤 함수의 인자가 변하지 않았다면 이전 인자를 꺼내서 사용할 수 있다.
st.title("Understanding st.cach_data")

# Function to simulate an expensive computation
@st.cache_data
def expensive_computation(arg1):
    time.sleep(2)
    st.write(f"argument는 {arg1}")
    result = np.random.rand() + arg1
    return result

if st.button("Run expensive computation"):
    result1 = expensive_computation(np.random.rand())
    st.write(f"argument가 변경되면 {result1} 결과는 변경")

if st.button("Run cache computation"):
    result2 = expensive_computation(100)
    st.write(f"argument가 변경안되면 {result2} 결과는 고정")
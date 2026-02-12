import streamlit as st

st.title("知识库更新服务")

upload_file = st.file_uploader(
    "请上传txt文件",
    type=['txt'],
    accept_multiple_files=False
)

if upload_file is not None:
    file_name = upload_file.name
    file_type = upload_file.type
    file_size = upload_file.size / 1024
    st.subheader(f"文件名: {file_name}")
    st.write(f"文件类型: {file_type} | 文件大小: {file_size} KB")

    text = upload_file.getvalue().decode("UTF-8")
    st.write(text)
    st.success("上传成功")
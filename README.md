# RAGDemo
qwen-7b-chat、LlamaIndex

## 简述:本文档通过使用LLamaIndex结合qwen-7b-chat实现了一个RAG搜索系统，亲测能正常运行;过程踩了一些坑；需要了解的可以详聊；

## 安装运行环境
```bash
1，python及其依赖的环境安装
# 创建虚拟环境
python -m venv myenv

# 激活虚拟环境
.\myenv\Scripts\activate

# 更新pip版本;
python.exe -m pip install --upgrade pip

# 安装sentence-transformers库
pip install sentence-transformers

# 安装其它依赖
pip install llama-index langchain aliyun-python-sdk-core-v3 aliyun-python-sdk-ga requests tqdm numpy


pip install dashscope

pip install IPython

pip install llama-index-embeddings-huggingface

pip install hf_xet

2，申请阿里key
用于替换 rag_with_tongyiqianwen.py中的dashscope.api_key = "sk-xxxxx" 值;

3, 下载 rag_with_tongyiqianwen.py并修改

4，运行
(myenv) PS C:\E\ai_project> python.exe .\rag_with_tongyiqianwen.py

```

## 资源说明
### rag_with_tongyiqianwen.py demo源码
### doc/pip_list.txt 我本机myenv的pip list得到结果
### doc/RAGDemo_Run_Result.jpg 运行成功的截图
## data/example.txt 随机生成的一段小文章,可以认为待处理的数据
### doc/《森林中的暗战》-豆包.png 生成 data/example.txt 的豆包交互截图


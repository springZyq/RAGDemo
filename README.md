# RAGDemo
qwen-7b-chat、LlamaIndex

## 本文档通过使用LLamaIndex结合qwen-7b-chat实现了一个RAG搜索系统，亲测能正常运行;过程踩了一些坑；需要了解的可以详聊；

## 安装环境
```bash
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

```


## doc下有运行出来的效果《RAGDemo_Run_Result.jpg》截图；
## data下的数据example.txt 使用 doc下《《森林中的暗战》-豆包.png》 方法随意创建的一片小文章;

import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.llms import CustomLLM
from dashscope import Generation
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import dashscope
# 设置通义千问的API密钥
dashscope.api_key = "sk-xxxxx"


# 自定义一个元数据类
class LLMMetadata:
    def __init__(self, name, context_window,num_output):
        self.name = name
        self.context_window = context_window
        self.num_output = num_output
        self.is_chat_model = False

# 自定义一个包含 text 属性的类
class CompletionResponse:
    def __init__(self, text):
        self.text = text

# 自定义LLM类以集成通义千问
class TongyiQianwenLLM(CustomLLM):
    @property
    def metadata(self):
        return LLMMetadata(name="TongyiQianwen", context_window=4096,num_output = -1)  # 假设上下文窗口大小为 4096

    @property
    def model_name(self):
        return "qwen-7b-chat"

    def complete(self, prompt, **kwargs):
        print("开始调用通义千问进行文本生成...")
        response = Generation.call(
            model=self.model_name,
            prompt=prompt,
            **kwargs
        )
        print("通义千问文本生成完成。")
        # 返回一个包含 text 属性的对象
        return CompletionResponse(response.output.text)

    def stream_complete(self, prompt, **kwargs):
            # 这里简单模拟流式输出，实际使用时需要根据通义千问的流式API进行实现
            import time
            response = self.complete(prompt, **kwargs)
            for char in response:
                time.sleep(0.1)  # 模拟流式输出的延迟
                yield char        

print("开始加载数据...")
# 加载数据
# documents = SimpleDirectoryReader('.\\data1\\paul_graham\\').load_data()
documents = SimpleDirectoryReader('C:\\E\\ai_project\\data\\').load_data()
print(f"加载数据成功，加载了 {len(documents)} 个文档。")

print("开始初始化HuggingFaceEmbedding...")
embed_model = HuggingFaceEmbedding(model_name="all-MiniLM-L6-v2")
print(f"HuggingFaceEmbedding 成功初始化。")

print("开始创建索引...")
# 创建索引
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
print(f"VectorStoreIndex 成功创建。")

print("开始创建查询引擎...")
# 创建查询引擎
query_engine = index.as_query_engine(
    llm=TongyiQianwenLLM(),
    similarity_top_k=3 
)
print("查询引擎创建成功。")

print("开始进行查询...")
# 进行查询
response = query_engine.query("文中有几个人物,他们的角色分别是什么?")
print(f"查询完成，结果如下：{response}")
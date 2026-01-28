import gradio as gr


def dummy_transcribe(audio):
    """占位推理函数：不真正调用 Whisper，仅模拟输出。"""
    return "这是 Whisper-medium WebUI 的示例转写结果，用于界面展示，不执行真实模型推理。"


def build_interface():
    with gr.Blocks(title="Whisper-medium WebUI") as demo:
        gr.Markdown("""# Whisper-medium WebUI

本演示界面模拟 Whisper-medium 语音识别与翻译流程，仅用于前端可视化展示。""")
        with gr.Row():
            with gr.Column(scale=2):
                audio_in = gr.Audio(sources=["upload", "microphone"], type="filepath", label="语音输入")
                lang = gr.Dropdown([
                    "自动检测",
                    "英语 English",
                    "中文 Chinese",
                    "法语 French",
                    "德语 German",
                ], value="自动检测", label="语种/任务选择")
                run_btn = gr.Button("开始转写 / 翻译")
            with gr.Column(scale=3):
                text_out = gr.Textbox(label="文本输出", lines=8)
                gr.Markdown("""可在右侧区域查看转写文本、时间轴与置信度等可视化结果。""")

        run_btn.click(fn=dummy_transcribe, inputs=audio_in, outputs=text_out)
    return demo


if __name__ == "__main__":
    demo = build_interface()
    demo.launch()

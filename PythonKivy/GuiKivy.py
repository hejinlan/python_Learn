# _*_ coding : UTF-8 _*_
# 微信公众号： xiaoqiangclub
# 开发时间： 2021/7/22  13:42
# 文件名称： TTS.py
# 开发工具： PyCharm
# Text to speech
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder


class Test(Widget):
    pass


# Builder.load_file("kv/tts.kv")  # 导入kv文件
Builder.load_string(
    """
# 注意：这里需要顶格写，否则会报错！
<Test>:
    Button:
        text: "XiaoqiangClub"
    """
)


class TTSApp(App):
    def build(self):
        # return Button(text="hello")   # 这是我们以前最简单的一个示例
        return Test()


if __name__ == '__main__':
    TTSApp().run()

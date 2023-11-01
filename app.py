import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

# Change the host to the IP address of your virtual machine
demo.launch(share=True)



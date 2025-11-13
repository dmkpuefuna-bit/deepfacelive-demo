import gradio as gr
from PIL import Image

def face_swap(source_img, target_img):
    """
    Simulates a face swap by blending two images.
    Lightweight demo version of DeepFaceLive.
    """
    source = source_img.convert("RGBA")
    target = target_img.convert("RGBA").resize(source.size)
    blended = Image.blend(source, target, alpha=0.5)
    return blended

# Custom CSS for styling
custom_css = """
body {
    background-color: #0B1120; /* Dark navy background */
    color: #E2E8F0; /* Light gray text */
    font-family: 'Poppins', sans-serif;
}

h1, .gr-title {
    color: #FF7A00; /* Orange title */
}

.gr-input_label, .gr-output_label {
    color: #38BDF8; /* Blue labels */
}

.gr-button {
    background-color: #FF7A00 !important; 
    color: white !important;
    border-radius: 8px;
}
"""

# Create Gradio interface
demo = gr.Interface(
    fn=face_swap,
    inputs=[
        gr.Image(label="Source Face", type="pil"),
        gr.Image(label="Target Face", type="pil")
    ],
    outputs=gr.Image(label="Swapped Output"),
    title="Daniel's DeepFaceLive Demo (Simplified)",
    description="Upload two face images to see a simulated swap demo. "
                "Full DeepFaceLive runs locally with GPU acceleration.",
    css=custom_css  # apply custom styling
)

if __name__ == "__main__":
    demo.launch()
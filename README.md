# LLM-Based LinkedIn Post Generator

An AI-powered tool that generates LinkedIn posts using Deepseek LLM running locally through Ollama. This tool helps create engaging LinkedIn content while maintaining full privacy and control over the generation process.

## 🚀 Features

- Generate engaging LinkedIn posts locally without relying on external APIs
- Runs completely offline using [deepseek-r1:1.5b](https://ollama.com/library/deepseek-r1:1.5b)  model through Ollama
- Customizable post topics and length.
- No API costs or usage limits
- Full privacy - all processing happens on your machine

## 📋 Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed on your system
- Deepseek model pulled via Ollama
- Required Python packages (listed in requirements.txt)

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/virajyadav/LLM_Based_Linkedin_Post_Generator.git
cd LLM_Based_Linkedin_Post_Generator
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Install Ollama following the instructions at [ollama.ai](https://ollama.ai)

4. Pull the Deepseek model:
```bash
ollama pull deepseek-r1:1.5b
```

## 💻 Usage

1. Ensure Ollama is running in the background
2. Run the generator:
```bash
streamlit run main.py
```


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ollama](https://ollama.com/) for providing the local model serving infrastructure
- [Deepseek](https://deepseek.com/) for their excellent language model
- LinkedIn influencer [Dhaval Patel](https://www.linkedin.com/in/dhavalsays/) whose styles inspire this project
- Contributors and supporters



---

Made with ❤️ by Viraj

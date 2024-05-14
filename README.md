# Alfred

## Introduction
As the demand for smart home systems and IoT devices continues to rise, there's a growing need for natural language processing to control these devices. This project proposes a solution using large language models (LLMs) to not only process simple commands but also understand and execute complex instructions through planning and reasoning. Integration with new devices and APIs is also made easier using code generation functions of LLMs.

## Features
- Utilizes large language models for advanced planning and reasoning in smart home automation.
- Streamlines the process by replacing multiple stages of traditional speech-processing pipelines.
- Introduces a multitask prompting format for correct task generation and JSON format outputs.
- Demonstrates strong generalization capabilities across different datasets and domains without fine-tuning.

## Architecture
![Architecture](/media/architecture.jpeg)
The system uses a pipeline approach:
- **Audio Input and Processing:** Whisper model converts speech to text.
- **Planning of Tasks:** Langchain framework extracts user intentions and generates actionable JSON commands.
- **JSON Extraction:** TinyLLaMA and GPT-3.5-turbo work together to generate structured JSON outputs compatible with smart home management systems (e.g., Google Nest).

## Running the model
Run the system by first installing and running the LLaMafile server. Then please install pyaudio according to your specific system. Next please install the requirements by running 

```console
pip install -r requirements.txt
```

Finally execute the system pipeline by 

```console
python main_run.py
```
## Demo
The demo video can be viewed from the media folder at demo.mkv
## Evaluation
The system was tested using a dataset of various prompts, ranging from simple to complex.  The results showed that the LLM-based approach(TinyLLaMA + ChatGPT) with LLM chaining, is effective in generating correct JSON outputs for controlling smart home devices.

## Installations
[Link](https://python.langchain.com/v0.1/docs/integrations/llms/llamafile/) to install LLaMafile.

## Link to Report
[Here](https://1drv.ms/b/s!AmvuLtjazyPDgcgl7yuxoWsq_TtY0g?e=Dw8xfL) is the link to the report.

## Authors
- Swaroop Ranganath
- Vishal Varma Kovoru

## Acknowledgements
- We would like to thank Professor Yang, Wei for giving us this opportunity.

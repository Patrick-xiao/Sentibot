# Sentiment Analysis Project

This project aims to fine-tune a BERT model using a dataset containing text and label for sentiment analysis. It includes both the training process and an online deployment for real-time sentiment prediction.

## Project Structure

### Online_Deployment

- **sentibot_online.html**: A static HTML file that serves as a web interface for sentiment analysis. Users can input text and get the sentiment prediction directly on this webpage.
- **Sentibot_website.txt**: Contains the link to the deployed static webpage on a server. You can visit this link to use the sentiment analysis tool online.

### Sentibot_training

- **Sentibot_training.ipynb**: The core Jupyter Notebook file that contains the complete training process of the BERT model. It includes data preprocessing, model fine-tuning, and evaluation.
- **performance_evaluation4.csv**: A CSV file that records the performance of the trained model. It has three columns: `text`, `sentiment`, and `predict_sentiment`, showing the original text, true sentiment, and predicted sentiment respectively.
- **sentiment_analysis.csv**: The original dataset used for training the BERT model. It contains the text samples along with their corresponding sentiment labels.

## Getting Started

### Prerequisites

- Python 3.x
- Libraries: transformers, torch, pandas, etc. (You can install them using `pip install transformers torch pandas`)

### Training the Model

1. Clone this repository to your local machine.
2. Navigate to the `Sentibot_training` folder.
3. Open `Sentibot_training.ipynb` in Jupyter Notebook.
4. Follow the steps in the notebook to preprocess the data, fine-tune the BERT model, and evaluate its performance.

### Using the Online Deployment

1. Visit the link provided in the `Sentibot_website.txt` file.
2. Enter the text you want to analyze in the input box on the webpage.
3. The sentiment prediction will be displayed immediately.

## Contributing

Feel free to fork this repository and make your own improvements. If you have any suggestions or find any issues, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

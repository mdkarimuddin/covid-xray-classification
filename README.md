# COVID-19 X-ray Classification with Flask

Deep learning project for classifying chest X-ray images into COVID-19, Normal, and Pneumonia categories using EfficientNet CNN, with a Flask web application for predictions.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![ML](https://img.shields.io/badge/ML-Deep%20Learning%20%7C%20CNN-orange.svg)
![Framework](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)

## 🎯 Project Overview

This project demonstrates:
- ✅ **Deep Learning**: EfficientNet CNN for medical image classification
- ✅ **Web Application**: Flask API for real-time predictions
- ✅ **Medical AI**: COVID-19 detection from chest X-ray images
- ✅ **Production Ready**: Complete pipeline from training to deployment

## 📊 Features

- **Multi-class Classification**: COVID-19, Normal, Pneumonia
- **EfficientNet Architecture**: State-of-the-art CNN for image classification
- **Flask API**: RESTful endpoint for predictions
- **Jupyter Notebooks**: Training and inference workflows

## 🗂️ Project Structure

```
Covid_Xray_Classification/
├── notebooks/
│   └── Flask_App_covid-xray-cleaned.ipynb  # Training and inference notebook
├── app.py                                   # Flask web application
├── requirements.txt                         # Python dependencies
├── models/                                  # Saved model files (not included)
├── data/                                    # Dataset directory (not included)
├── LICENSE
└── README.md
```

## 🚀 Quick Start

### Prerequisites

```bash
pip install -r requirements.txt
```

### Running the Flask App

```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000`

### API Endpoint

**POST** `/predict`
- **Input**: X-ray image file
- **Output**: JSON with prediction and confidence score
  ```json
  {
    "pred": "normal",
    "confidence": 0.78
  }
  ```

### Training the Model

1. Open `notebooks/Flask_App_covid-xray-cleaned.ipynb` in Jupyter/Colab
2. Follow the notebook to train the EfficientNet model
3. Save the trained model to `models/` directory

## 🔬 Methodology

- **Model Architecture**: EfficientNet (PyTorch)
- **Dataset**: Chest X-ray images (COVID-19, Normal, Pneumonia)
- **Preprocessing**: Image resizing, normalization
- **Training**: Transfer learning with fine-tuning

## 🛠️ Technologies

- **Python 3.8+**
- **PyTorch** - Deep learning framework
- **Flask** - Web framework
- **EfficientNet** - CNN architecture
- **PIL/Pillow** - Image processing
- **NumPy, Pandas** - Data manipulation

## 📝 Notes

- Model weights are not included in the repository (too large)
- Download dataset from appropriate medical imaging sources
- The `app.py` includes a placeholder prediction function - replace with actual model loading

## 👤 Author

**Md Karim Uddin, PhD**  
PhD Veterinary Medicine | MEng Big Data Analytics  
Postdoctoral Researcher, University of Helsinki

- GitHub: [@mdkarimuddin](https://github.com/mdkarimuddin)
- LinkedIn: [Md Karim Uddin, PhD](https://www.linkedin.com/in/md-karim-uddin-phd-aa87649a/)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**⭐ Star this repo if you found it useful!**

*Built to demonstrate deep learning capabilities for medical image classification.*

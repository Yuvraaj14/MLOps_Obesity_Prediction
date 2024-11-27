# Use an appropriate base image for Streamlit
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the Streamlit application files
COPY . .

# Expose the port for Streamlit
EXPOSE 8501

# Start the Streamlit app
CMD ["streamlit", "run", "StreamLit.py"]

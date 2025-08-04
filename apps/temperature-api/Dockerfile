# Используем официальный Python образ
FROM python:3.11-slim

# Рабочая директория
WORKDIR /app

# Копируем requirements и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY temperature-api-app.py .

# Открываем порт 8081
EXPOSE 8081

# Команда для запуска приложения
CMD ["python", "temperature-api-app.py"]



# Build stage
#FROM golang:1.22-alpine AS builder

# Set working directory
#WORKDIR /app

# Copy go.mod and go.sum files
#COPY go.mod go.sum ./

# Download dependencies
#RUN go mod download

# Copy the source code
#COPY . .

# Build the application
#RUN CGO_ENABLED=0 GOOS=linux go build -o temperature-api

# Runtime stage
#FROM alpine:latest

# Install necessary runtime dependencies
#RUN apk --no-cache add ca-certificates tzdata

# Set working directory
#WORKDIR /app

# Copy the binary from the builder stage
#COPY --from=builder /app/temperature-api .

# Expose the port the app runs on
#EXPOSE 8081

# Command to run the application
#CMD ["./temperature-api"]
# Sakura Dreams - Premium Anime Landing Page

A beautiful, high-end anime-themed landing page featuring modern web effects, glassmorphism, and a premium aesthetic.

## ✨ Features

- **🌸 Interactive Sakura Effects**: Smooth, performance-optimized falling cherry blossom petals powered by Anime.js.
- **💎 Glassmorphism Design**: Modern UI with frosted glass effects, deep backdrop blurs, and neon glowing borders.
- **🎭 Character Showcase**: Elegant character cards with hover effects and scroll-triggered animations.
- **📱 Responsive Layout**: Fully responsive design that looks great on all devices.
- **✨ Premium Typography**: Optimized font pairings using 'Syne' for headings and 'Inter' for body text.
- **🚀 Scroll Animations**: Smooth reveal animations as you explore the page.

## 🛠️ Technologies Used

- **HTML5 & CSS3**: Custom styles with advanced CSS features (Flexbox, Grid, Glassmorphism, CSS Variables).
- **JavaScript (ES6+)**: Custom interaction logic and intersection observers.
- **Anime.js**: Used for the sophisticated sakura petal physics and animations.
- **Google Fonts**: Premium typography integration.
- **Lucide Icons**: Clean and modern iconography.

## 🚀 Getting Started

### Prerequisites

- A modern web browser.
- (Optional) Docker for containerized deployment.

### Running Locally

1. Clone the repository.
2. Open `src/index.html` in your favorite web browser.

### Running with Docker

You can easily serve the website using Docker:

```bash
# Build the image
docker build -t sakura-dreams .

# Run the container
docker run -d -p 8080:80 sakura-dreams
```

Then visit `http://localhost:8080` in your browser.

## 🌐 Deployment Guide

### 🐙 Deploying to GitHub Pages (Recommended)

Since the project source is in the `src/` directory, the easiest way to deploy is using GitHub Actions:

1. Push your code to a GitHub repository.
2. Go to **Settings** > **Pages**.
3. Under **Build and deployment** > **Source**, select **GitHub Actions**.
4. The included `deploy.yml` workflow (if present) will automatically handle the deployment from the `src/` folder whenever you push to the `main` branch.

### ⚡ Deploying to Netlify / Vercel / Render

1. Connect your GitHub repository to Netlify, Vercel, or Render.
2. Configure the **Build Settings**:
   - **Build Command**: (Leave blank)
   - **Publish Directory**: `src`
3. Click **Deploy**.

## 🧪 Testing

The project includes automated UI tests using Python and Playwright.

```bash
# Install dependencies
pip install playwright pytest
playwright install chromium

# Run automated checks
python3 tests/check_elements.py
```

## 📜 License

This project is open-source and available under the MIT License.

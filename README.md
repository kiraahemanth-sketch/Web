# OTAKUSTAR - Ultimate Premium Anime Landing Page

A beautiful, high-end anime-themed landing page featuring modern web effects, glassmorphism, and a premium aesthetic. Dedicated to the ultimate anime fans at OTAKUSTAR.com.

## ✨ Features

- **🛡️ Google reCAPTCHA v3**: Built-in security integration for bot protection.
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
docker build -t otakustar .

# Run the container
docker run -d -p 8080:80 otakustar
```

Then visit `http://localhost:8080` in your browser.

## 🛡️ Security Note (reCAPTCHA v3)

Google reCAPTCHA v3 is integrated into this site.
- **Site Key**: `6LdsQmwsAAAAADkfFk-bubhm4D9VuL9at3ZYdQZx`
- **Frontend**: The `script.js` handles token generation on page load and button clicks.
- **Backend Verification**: You must use your **Secret Key** on your backend server to verify the tokens.
  - Ensure the Secret Key is stored securely as an environment variable (e.g., `RECAPTCHA_SECRET_KEY`).
  - **Security Warning**: Never expose the Secret Key in frontend code or commit it to a public repository.

## 🌐 Deployment Guide

### 🐙 Deploying to GitHub Pages (Recommended)

Since the project source is in the `src/` directory, the easiest way to deploy is using GitHub Actions:

1. Push your code to a GitHub repository.
2. Go to **Settings** > **Pages**.
3. Under **Build and deployment** > **Source**, select **GitHub Actions**.
4. The included `deploy.yml` workflow (if present) will automatically handle the deployment from the `src/` folder whenever you push to the `main` branch.

### ⚡ Deploying to Netlify / Vercel / Render

1. Connect your GitHub repository to Netlify, Vercel, or Render.
2. **IMPORTANT**: Configure the **Publish Directory** (or **Root Directory**) to `src`.
   - If you don't do this, you will get a "Page Not Found" (404) error because the website files are inside the `src` folder.
   - For Netlify, a `netlify.toml` is included to handle this automatically.
   - For Vercel, set the "Root Directory" to `src` in your project settings.
3. **Build Command**: Leave blank.
4. Click **Deploy**.

#### 📂 Note on Drag-and-Drop
If you are using Netlify's "Drag and Drop" feature instead of Git:
- **Do not** drag the whole project folder.
- **Only** drag the contents of the `src` folder.

## 🧪 Testing

The project includes automated UI tests using Python and Playwright.

```bash
# Install dependencies
pip install playwright pytest
playwright install chromium

# Run automated checks
python3 tests/verify_otakustar.py
```

## 📜 License

This project is open-source and available under the MIT License.

import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
// https://vitejs.dev/config/
export default defineConfig({
    plugins: [react()],
    server: {
        fs: {
            allow: ["./src"], // Allows serving files from the project root
        },
        proxy: {
            // Proxy API requests to the backend server
            '/api': {
                target: 'http://localhost:8000',
                changeOrigin: true,
                secure: false
            },
            // Proxy config.json requests to the backend server
            '/config.json': {
                target: 'http://localhost:8000',
                changeOrigin: true,
                secure: false
            }
        }
    },
    build: {
        outDir: "dist",
        chunkSizeWarningLimit: 1000, // Increase warning limit (optional)
    },
    define: {
        "import.meta.env": {}, // Ensures compatibility with Vite env system
    },
});

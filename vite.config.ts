import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react';
import path from 'path';
import { defineConfig } from 'vite';

export default defineConfig(() => {
  return {
    plugins: [
      react(), 
      tailwindcss(),
      {
        name: 'mock-api',
        configureServer(server) {
          server.middlewares.use('/customer-preferences/api/flyout/xop-and-country', (req, res) => {
            res.setHeader('Content-Type', 'application/json');
            res.end(JSON.stringify({}));
          });
        },
        configurePreviewServer(server) {
          server.middlewares.use('/customer-preferences/api/flyout/xop-and-country', (req, res) => {
            res.setHeader('Content-Type', 'application/json');
            res.end(JSON.stringify({}));
          });
        }
      }
    ],
    resolve: {
      alias: {
        '@': path.resolve(__dirname, '.'),
      },
    },
    server: {
      hmr: process.env.DISABLE_HMR !== 'true',
      watch: process.env.DISABLE_HMR === 'true' ? null : {},
    },
  };
});

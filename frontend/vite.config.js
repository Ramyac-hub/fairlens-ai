import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        analysis: resolve(__dirname, 'analysis.html'),
        simulation: resolve(__dirname, 'simulation.html'),
        'multi-domain': resolve(__dirname, 'multi-domain.html'),
        'bias-explanation': resolve(__dirname, 'bias-explanation.html')
      }
    }
  }
})
import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        analysis: resolve(__dirname, 'analysis.html'),
        simulation: resolve(__dirname, 'simulation.html'),
        multidomain: resolve(__dirname, 'multidomain.html'),
        biasexplanation: resolve(__dirname, 'biasexplanation.html')
      }
    }
  }
})
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  build: {
    rollupOptions: {
      input: {
        main: 'index.html',
        analysis: 'analysis.html',
        multidomain: 'multi-domain.html',
        biasexplanation: 'bias-explanation.html',
        simulation: 'simulation.html'
      }
    }
  }
})
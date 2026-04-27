import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  build: {
    rollupOptions: {
      input: {
        main: 'index.html',
        analysis: 'analysis.html',
        multi-domain: 'multi-domain.html',
        bias-explanation: 'bias-explanation.html',
        simulation: 'simulation.html',
      }
    }
  }
})
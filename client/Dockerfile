# Usa uma imagem Node.js leve
FROM node:18-alpine

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do package.json e package-lock.json antes para otimizar cache
COPY package.json package-lock.json ./

# Instala as dependências
RUN npm install

# Copia o restante da aplicação para dentro do container
COPY . .

# Expõe a porta do Vite para desenvolvimento
EXPOSE 5173

# Comando para iniciar o servidor de desenvolvimento
CMD ["npm", "run", "dev", "--", "--host"]

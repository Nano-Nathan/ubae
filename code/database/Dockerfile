# Utilizar una imagen base de Node.js
FROM node:lts-alpine

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar los archivos package.json y package-lock.json
COPY package*.json ./

# Instalar las dependencias del proyecto
RUN npm install

# Copiar el código fuente de la aplicación
COPY . .

# Exponer el puerto 3000 en el contenedor
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD [ "node", "index.js" ]
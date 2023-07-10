server {
    listen 80;
    server_name myconvenient.com;

    location / {
        proxy_pass https://my-convenients.onrender.com;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

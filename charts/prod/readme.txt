
helm install app-prod --namespace prod ./prod/ -f ./prod/values.yaml
helm uninstall app-prod -n prod

commande debug:

helm status app-dev
helm --debug status app-dev
helm list --all --namespace devj
kubectl get all --all-namespaces
kubectl config viewc

------

Accéder à l'application :
http://34.253.0.239:31100/docs
curl -X POST -H "Content-Type: application/json" -d '{"username":"admin","password":"a"}' http://34.253.0.239:31700/api/login
{"id":1,"username":"admin","email":"admin@baran.com","full_name":"Admin Admin","user_type":"admin","hashed_password":"$2b$12$16kNu5IW80k1Tw7xz2H3iOCsz0.oMZ7q5OSGa/OIfOae0WGFe8aI2","created_by":1}
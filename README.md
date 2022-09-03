# hsa_stress_testing

# Simple FastAPI api generate data and put to Postgres DB
## URLs:
/  
/generate_user  
/generate_page  
/generate_numner  

## Run containers
```docker-compose up```  

## Results
#concurrent | #availability | #avg response time, secs | #throughput, MB/sec |  
--- | --- | --- | --- |  
10 | 100% | 0.08 | 0.01 |  
25 | 100% | 0.27 | 0.01 |  
50 | 100% | 0.45 | 0.01 |  
100 | 100% | 0.86 | 0.01 |  


## Siege commands
Commands:  
```siege -c 10 --time=60S -f urls.txt -i --log='concurrent_10.log'```  
```siege -c 25 --time=60S -f urls.txt -i --log='concurrent_25.log'```  
```siege -c 50 --time=60S -f urls.txt -i --log='concurrent_50.log'```  
```siege -c 100 --time=60S -f urls.txt -i --log='concurrent_100.log'```  

## Execution logs
![Siege10](https://user-images.githubusercontent.com/52753625/188263335-531abbeb-d967-4962-9f50-9e89c2b1a822.PNG)  
![Siege25](https://user-images.githubusercontent.com/52753625/188263337-de86c33f-3ad1-4ebf-8f5c-54a087a516cb.PNG)  
![Siege50](https://user-images.githubusercontent.com/52753625/188263340-8804e7bc-a89b-456e-94d0-68f2bf566876.PNG)  
![Siege100](https://user-images.githubusercontent.com/52753625/188263341-647d28a4-802b-4784-bf68-a2bf25d1dbf2.PNG)  

## Api log
![App_log](https://user-images.githubusercontent.com/52753625/188263565-38f059f5-2a1f-4b7a-ac76-336c75f255a6.PNG)  

## Data sample view
![Data1](https://user-images.githubusercontent.com/52753625/188263572-165c7edf-8b50-473d-bff9-b8f64ee883ff.PNG)  
![Data2](https://user-images.githubusercontent.com/52753625/188263575-65c40ed5-9bc7-4dc3-a87d-13ad12d722b3.PNG)  

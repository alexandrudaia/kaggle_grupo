number_of_stores=length(table(train$Agencia_ID))
print(number_of_stores)

store_ids=unique(train$Agencia_ID)
dimmensions=c()

for(store in  store_ids)
{
  current_store=train[train$Agencia_ID==store,]
  dimmensions=c(dimmensions,dim(current_store)[1])
  store_name=paste0("store",toString(store),".csv")
  write.csv(current_store,store_name)
  
}


#library(sqldf) # fast things
#store1<- read.csv.sql("/media/machine_learning/A80C461E0C45E7C0/bilboa/train.csv", 
#                     sql = "select * from file where Agencia_ID==1110", eol = "\n")
#write.csv( store1,"/media/machine_learning/A80C461E0C45E7C0/bilboa/store1.csv",row.names = F)

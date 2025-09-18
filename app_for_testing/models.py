from django.db import models




class Fields_Exemples(models.Model):  
# ========================================== Field options ==========================================

    # null : Si True, Django stockera les valeurs vides comme NULL dans la base de données. La valeur par défaut est False
    date = models.DateField(null=True) 

    # blank : Si True, le champ est autorisé à être vide. La valeur par défaut est False
    name = models.CharField(max_length=50, blank=True)

    # choices : sert à limiter les valeurs possibles d’un champ (par exemple, un statut)
    STATUS_CHOICES = [
        ("CLEAN", "Clean"),
        ("SOON", "Replace Soon"),
        ("NOW", "Replace Now"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="CLEAN")
    
    # db_column : Si tu veux donner un autre nom à la colonne dans la base, tu utilises db_column
    brand = models.CharField(max_length=50, db_column="filter_brand")

    # db_default : Elle définit la valeur par défaut directement au niveau de la base de données
    status = models.CharField(max_length=20, db_default="Clean")  
    
    # editable : Définit si un champ est modifiable dans l’admin Django et les formulaires (default = true)
    created_at = models.DateTimeField(auto_now_add=True, editable=False) 
    
    # primary_key : Définit un champ comme clé primaire de la table (identifiant unique)
    filter_id = models.IntegerField(primary_key=True)
    
    # unique :Sert à dire qu’une valeur ne peut pas se répéter dans la base de données
    email = models.EmailField(unique=True) 

# ========================================== Field types ==========================================

    # CharField :Texte court (nécessite 'max_length')    
    name = models.CharField(max_length=100)                       

    # TextField : Texte long (paragraphe)
    bio = models.TextField()

    # IntegerField : Entier (positif ou négatif) 
    age = models.IntegerField()

    # PositiveIntegerFieldEntier : positif uniquement            
    score = models.PositiveIntegerField()
    
    # FloatField : Nombre décimal flottant
    price = models.FloatField()
   
    # DecimalField : Nombre décimal précis
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    # BooleanField : Vrai / Faux                    
    is_active = models.BooleanField(default=True)                

    # DateField : Date uniquement                        
    birth_date = models.DateField()                              
    
    # TimeField : Heure uniquement                       
    start_time = models.TimeField()                              
    
    # DateTimeField : Date + heure                           
    created_at = models.DateTimeField(auto_now_add=True)         
    
    # EmailField : Adresse email validée                  
    email = models.EmailField(unique=True)                       
    
    # URLField : lien web                               
    website = models.URLField()                                  
    
    # SlugField : Texte court sans espace (URL friendly) 
    slug = models.SlugField(unique=True)                         
    
    # FileField : Fichier uploadé                        
    file = models.FileField(upload_to="uploads/")                
    
    # ImageField : Image uploadée (besoin de Pillow)      
    photo = models.ImageField(upload_to="images/")               
    
    # BinaryField : Données binaires                       
    data = models.BinaryField()                                  
    
    # UUIDField : Identifiant unique (UUID)              
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    
    # ForeignKey : Relation plusieurs-à-un                
    author = models.ForeignKey(User, on_delete=models.CASCADE)   
    
    # OneToOneField : Relation un-à-un                       
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # ManyToManyField : Relation plusieurs-à-plusieurs         
    tags = models.ManyToManyField(Tag)                           


    def __str__(self):
        return self.brand  # Pour afficher le nom du filtre dans l’admin

from haystack import indexes

from django.utils import timezone

from .models import Product

# from django.conf import settings
from haystack.backends.elasticsearch_backend import (ElasticsearchSearchBackend,
    ElasticsearchSearchEngine)

# from haystack.query import SearchQuerySet





# class NoteIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     title = indexes.CharField(model_attr='title')
#     body = indexes.CharField(model_attr='body')

#     def get_model(self):
#         return Note

#     def index_queryset(self, using=None):
#         """Used when the entire index for model is updated."""
#         return self.get_model().objects.filter(timestamp__lte=timezone.now())

class ProductIndex(indexes.SearchIndex, indexes.Indexable):
	# content_auto = indexes.EdgeNgramField(model_attr='title')
	# content_auto = indexes.EdgeNgramField(model_attr='title')
  	text = indexes.NgramField(document=True,model_attr='title')
  	title=indexes.CharField(model_attr='title')
  	# photo = indexes.ImageField(upload_to='static/img')
  	price = indexes.FloatField(model_attr='price')
  	description = indexes.CharField(model_attr='description')
  	# timestamp = indexes.DateTimeField(model_attr='timestamp',null=True)

	def get_model(self):
	    return Product

	def index_queryset(self, using=None):
	    """Used when the entire index for model is updated."""
	    return self.get_model().objects.filter(timestamp__lte=timezone.now())



# sqs = SearchQuerySet().filter(content_auto=request.GET.get('q', ''))

# SearchQuerySet().autocomplete(content_auto='old')
# # Result match things like 'goldfish', 'cuckold' and 'older'.

# SearchQuerySet().autocomplete(content_auto='car')
# Result match things like 'goldfish', 'cuckold' and 'older'.

# SearchQuerySet().filter(title_element=clean_value)


#Mapping:

# "ngram": {
#   "type":"string",
#   "search_analyzer":"lowercase_analyzer",
#   "index_analyzer":"nGram_index_analyzer"
# }


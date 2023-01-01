# Serializer Field
# Serializer Field handle converting between primitive values and internal datatypes.
# They also deal with validating input values,as well as retrieving and setting the values from their parents objects.
# CharField(max_length=None,min_length=None,allow_blank=False,trim_whitespace=True)
# IntegerField(max_length=None,min_length=None)
# FloatField(max_length=None,min_length=None)
# DecimalField(max_digits,decimal_places,coerce_to_string=None,max_value=None,min_value=None)
# SlugField(max_length=None,min_length=None,allow_blank=False)
# EmailField(max_length=None,min_length=None,allow_blank=False)
# UrlField(max_length=None,min_length=None,allow_blank=False)
# BooleanField()
# NullBooleanField()
# FileField(max_length=None,allow_empty_file=False,use_url=UPLOADED_FILES_USE_URL)
# ImageField(max_length=None,allow_empty_file=False,use_url=UPLOADED_FILES_USE_URL)
# DateField(format=api_settings.DATE_FORMAT,input_formats=None)
# TimeField(format=api_settings.TIME_FORMAT,input_formats=None)
# DateTimeField(format=api_settings.DATETIME_FORMAT,input_formats=None,default_timezone=None)
# DurationField(max_value=None,min_value=None)
# RegexField(regex,max_length=None,min_value=None,allow_blank=False)
# UUIDField(format="hex_verbose")
# FilePathField(path,match=None,recursive=False,allow_files=True,allow_folders=False,required=None,**kwargs)
# IPAddressField(protocol="both",unpack_ipv4=False,**options)
# ChoiceField(choices)
# MultipleChoiceField(choices)
# ListField(child=<A_FIELD_INSTANCE>,allow_empty=True,min_length=None,max_length=None)
# DictField(child=<A_FIELD_INSTANCE>,allow_empty=True,min_length=None,max_length=None)
# HStoreField(child=<A_FIELD_INSTANCE>,allow_empty=True,min_length=None,max_length=None)
# JSONField(binary.encoder)
# ReadOnlyField()
# HiddenField()
# ModelField()
# SerializerMethodField(method_name=None)


# Core Arguments
# label
# validators
# error_messages
# help_text
# required
# default
# initial
# style
# password=serializers.CharField(max_length=100,style={"input_type":"password","placeholder":"Password"})
# read_only
# write_only
# allow_null
# source


# Desrializations
# BytesIO()   stream=io.BytesIO(json_data) jsondata to stream
# JSONParser()
    # This is used to parse json data to python native data.
    # from rest_framework.parsers import JSONParser
    # parsed_data=JOSNParser().parse(stream)

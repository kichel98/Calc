# DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addArg1Arg2Get**](DefaultApi.md#addArg1Arg2Get) | **GET** /add/{arg1}/{arg2} | 
[**divideArg1Arg2Get**](DefaultApi.md#divideArg1Arg2Get) | **GET** /divide/{arg1}/{arg2} | 
[**multiplyArg1Arg2Get**](DefaultApi.md#multiplyArg1Arg2Get) | **GET** /multiply/{arg1}/{arg2} | 
[**substractArg1Arg2Get**](DefaultApi.md#substractArg1Arg2Get) | **GET** /substract/{arg1}/{arg2} | 

<a name="addArg1Arg2Get"></a>
# **addArg1Arg2Get**
> BigDecimal addArg1Arg2Get(arg1, arg2)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.DefaultApi;


DefaultApi apiInstance = new DefaultApi();
BigDecimal arg1 = new BigDecimal(); // BigDecimal | First element
BigDecimal arg2 = new BigDecimal(); // BigDecimal | Second element
try {
    BigDecimal result = apiInstance.addArg1Arg2Get(arg1, arg2);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#addArg1Arg2Get");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arg1** | **BigDecimal**| First element |
 **arg2** | **BigDecimal**| Second element |

### Return type

[**BigDecimal**](BigDecimal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="divideArg1Arg2Get"></a>
# **divideArg1Arg2Get**
> BigDecimal divideArg1Arg2Get(arg1, arg2)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.DefaultApi;


DefaultApi apiInstance = new DefaultApi();
BigDecimal arg1 = new BigDecimal(); // BigDecimal | Dividend
BigDecimal arg2 = new BigDecimal(); // BigDecimal | Divisor
try {
    BigDecimal result = apiInstance.divideArg1Arg2Get(arg1, arg2);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#divideArg1Arg2Get");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arg1** | **BigDecimal**| Dividend |
 **arg2** | **BigDecimal**| Divisor |

### Return type

[**BigDecimal**](BigDecimal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="multiplyArg1Arg2Get"></a>
# **multiplyArg1Arg2Get**
> BigDecimal multiplyArg1Arg2Get(arg1, arg2)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.DefaultApi;


DefaultApi apiInstance = new DefaultApi();
BigDecimal arg1 = new BigDecimal(); // BigDecimal | First factor
BigDecimal arg2 = new BigDecimal(); // BigDecimal | Second factor
try {
    BigDecimal result = apiInstance.multiplyArg1Arg2Get(arg1, arg2);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#multiplyArg1Arg2Get");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arg1** | **BigDecimal**| First factor |
 **arg2** | **BigDecimal**| Second factor |

### Return type

[**BigDecimal**](BigDecimal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="substractArg1Arg2Get"></a>
# **substractArg1Arg2Get**
> BigDecimal substractArg1Arg2Get(arg1, arg2)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.DefaultApi;


DefaultApi apiInstance = new DefaultApi();
BigDecimal arg1 = new BigDecimal(); // BigDecimal | Minuend
BigDecimal arg2 = new BigDecimal(); // BigDecimal | Subtrahend
try {
    BigDecimal result = apiInstance.substractArg1Arg2Get(arg1, arg2);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#substractArg1Arg2Get");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arg1** | **BigDecimal**| Minuend |
 **arg2** | **BigDecimal**| Subtrahend |

### Return type

[**BigDecimal**](BigDecimal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


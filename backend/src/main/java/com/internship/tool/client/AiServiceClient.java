package com.internship.tool.client;

import org.springframework.http.*;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.client.RestClientException;
import org.springframework.http.client.SimpleClientHttpRequestFactory;

import java.util.Map;
import java.util.HashMap;

public class AiServiceClient {

    private final RestTemplate restTemplate;
    private final String baseUrl;

    public AiServiceClient(String baseUrl) {
        this.baseUrl = baseUrl;
        this.restTemplate = new RestTemplate();
        SimpleClientHttpRequestFactory factory = new SimpleClientHttpRequestFactory();
        factory.setConnectTimeout(10000); // 10 seconds
        factory.setReadTimeout(10000);    // 10 seconds
        this.restTemplate.setRequestFactory(factory);
    }

    public String callHealth() {
        try {
            ResponseEntity<String> response = restTemplate.getForEntity(baseUrl + "/health", String.class);
            if (response.getStatusCode() == HttpStatus.OK) {
                return response.getBody();
            }
        } catch (RestClientException e) {
            // Log error if needed
        }
        return null;
    }

    public String callPrompt(String prompt) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);
            Map<String, String> body = new HashMap<>();
            body.put("prompt", prompt);
            HttpEntity<Map<String, String>> entity = new HttpEntity<>(body, headers);
            ResponseEntity<String> response = restTemplate.postForEntity(baseUrl + "/api/ai/prompt", entity, String.class);
            if (response.getStatusCode() == HttpStatus.OK) {
                return response.getBody();
            }
        } catch (RestClientException e) {
            // Log error if needed
        }
        return null;
    }
}
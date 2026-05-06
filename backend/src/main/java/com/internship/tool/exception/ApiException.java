package com.internship.tool.exception;

public class ApiException extends RuntimeException {
    public ApiException(String message) {
        super(message);
    }
}

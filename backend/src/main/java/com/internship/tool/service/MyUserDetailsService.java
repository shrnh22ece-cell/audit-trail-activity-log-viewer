package com.internship.tool.service;

import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import java.util.ArrayList;

@Service
public class MyUserDetailsService implements UserDetailsService {

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        // For demo, hardcode a user. In real app, load from DB.
        if ("user".equals(username)) {
            return new User("user", "{noop}password", new ArrayList<>()); // {noop} for plain text
        } else {
            throw new UsernameNotFoundException("User not found");
        }
    }
}
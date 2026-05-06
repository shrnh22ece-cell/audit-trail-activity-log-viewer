package com.internship.tool.service;

import com.internship.tool.entity.SampleEntity;
import com.internship.tool.repository.SampleRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class SampleService {

    private final SampleRepository sampleRepository;

    public SampleService(SampleRepository sampleRepository) {
        this.sampleRepository = sampleRepository;
    }

    public List<SampleEntity> getAllItems() {
        return sampleRepository.findAll();
    }
}

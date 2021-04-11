package com.lolin.service;

import org.springframework.web.multipart.MultipartFile;

public interface FileUploadService {

	public String fileUpload(MultipartFile file);

}

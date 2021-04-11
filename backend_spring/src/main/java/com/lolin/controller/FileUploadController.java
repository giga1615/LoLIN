package com.lolin.controller;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

import org.apache.commons.io.IOUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.util.Assert;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import com.lolin.service.FileUploadService;

@RestController
@RequestMapping("/api/file")
public class FileUploadController {

	@Autowired
	FileUploadService fileUploadService;

	@PostMapping("/upload")
	@ResponseBody
	public ResponseEntity<Map<String, Object>> fileUpload1(
			@RequestParam(value = "files", required = false) MultipartFile file) {
		Map<String, Object> resultMap = new HashMap<>();
		HttpStatus status = HttpStatus.OK;

		String check = fileUploadService.fileUpload(file);// 이거 파일업로드 실행하는거

		if (check.equals("Error")) {
			resultMap.put("message", "Fail");
			status = HttpStatus.INTERNAL_SERVER_ERROR;
		} else {
			resultMap.put("message", "SUCCESS");
			
			status = HttpStatus.OK;
		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);

	}

}

package com.lolin.controller;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import java.util.HashMap;
import java.util.Map;

import org.apache.commons.io.IOUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.lolin.service.PythonService;

@CrossOrigin(origins = { "*" }, maxAge = 6000)
@RestController
@RequestMapping("/api")
public class ImgController {

	
	@Autowired
	PythonService pythonService;

	// feed image 반환하기
	@GetMapping(value = "/image/{imagename}", produces = MediaType.IMAGE_JPEG_VALUE)
	public ResponseEntity<byte[]> userSearch(@RequestParam(value = "imagename", required = false) String imagename) throws IOException {

		String dir = StringUtils.cleanPath("/home/ubuntu/src/");
		InputStream imageStream = new FileInputStream(dir + imagename);

		byte[] imageByteArray = IOUtils.toByteArray(imageStream);

		imageStream.close();
		return new ResponseEntity<byte[]>(imageByteArray, HttpStatus.OK);

	}
	
}

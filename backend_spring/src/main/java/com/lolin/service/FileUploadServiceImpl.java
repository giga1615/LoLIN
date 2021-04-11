package com.lolin.service;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.springframework.stereotype.Service;
import org.springframework.util.Assert;
import org.springframework.util.StringUtils;
import org.springframework.web.multipart.MultipartFile;

@Service
public class FileUploadServiceImpl implements FileUploadService {

	@Override
	public String fileUpload(MultipartFile file) {
		SimpleDateFormat format1 = new SimpleDateFormat("yyyyMMddHHmmss");
		Date time = new Date();
		String plusTime = format1.format(time);


		String rootPath = "/home/ubuntu/src/";

		String filePath = rootPath + "/";

		Path directory = Paths.get(filePath).toAbsolutePath().normalize();

		plusTime.replaceAll(":", "");
		String fileName = StringUtils.cleanPath(plusTime + file.getOriginalFilename());

		String pathDB = "http://j4a104.p.ssafy.io:8080/lolin/image/" + fileName;

		Assert.state(!fileName.contains(".."), "Name of file cannot contain '..'");
		// 파일을 저장할 경로를 Path 객체로 받는다.
		Path targetPath = directory.resolve(fileName).normalize();

		// 파일이 이미 존재하는지 확인하여 존재한다면 오류를 발생하고 없다면 저장한다.
		Assert.state(!Files.exists(targetPath), fileName + " File alerdy exists.");
		try {
			file.transferTo(targetPath);
		} catch (IllegalStateException e) {

			e.printStackTrace();
			return "Error";
		} catch (IOException e) {

			e.printStackTrace();
			return "Error";
		}

		return pathDB;
	}

}

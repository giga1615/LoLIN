package com.lolin.controller;

import java.io.UnsupportedEncodingException;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.lolin.model.ConnectionDto;
import com.lolin.service.PythonService;

@CrossOrigin(origins = { "*" }, maxAge = 6000)
@RestController
@RequestMapping("/api/bigdata")
public class BigDataController {

	@Autowired
	PythonService pythonService;

	@GetMapping("/inGame")
	public ResponseEntity<Object> toPython(@RequestParam(value = "nickName", required = false) String nickName)
			throws UnsupportedEncodingException {
		nickName=nickName.replaceAll(" ", "");
		System.out.println("들어오긴하냐");

		Map<String, Object> resultMap = new HashMap<>();

		HttpStatus status = null;
		Object json = pythonService.getBigData(nickName);

		resultMap.put("컨트롤러에서 json보내줌", json);

		status = HttpStatus.ACCEPTED;

		return new ResponseEntity<Object>(json, status);

	}

}

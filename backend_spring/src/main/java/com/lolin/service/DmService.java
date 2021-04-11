package com.lolin.service;

import java.util.List;

import com.lolin.model.DmMessageDto;

public interface DmService {
	void sendDm(DmMessageDto sendMessage) throws Exception;

	List<DmMessageDto> readDmByNickName(String myNickName, String yourNickName) throws Exception;

	List<String> getDmList(String myId) throws Exception;
}

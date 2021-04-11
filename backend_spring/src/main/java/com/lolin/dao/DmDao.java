package com.lolin.dao;

import java.util.List;

import org.springframework.stereotype.Repository;

import com.lolin.model.DmMessageDto;

@Repository
public interface DmDao {
	void sendDm(DmMessageDto sendMessage) throws Exception;

	List<DmMessageDto> readDmByNickName(String myNickName, String yourNickName) throws Exception;

	List<String> getDmList(String myId) throws Exception;
}

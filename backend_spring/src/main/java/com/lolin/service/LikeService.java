package com.lolin.service;

import java.sql.SQLException;
import java.util.List;

import com.lolin.model.LikeDto;

public interface LikeService {

	// plus
	public void likePlus(String my_id, String my_nickname, String your_nickname) throws SQLException;

	// minus
	public void likeMinus(String my_nickname, String your_nickname) throws SQLException;

	// read
	public List<LikeDto> likeRead(String my_id) throws SQLException;

}

package com.lolin.dao;

import java.sql.SQLException;
import java.util.List;

import org.springframework.stereotype.Repository;

import com.lolin.model.LikeDto;

@Repository
public interface LikeDao {

	// plus
	public void likePlus(String my_nickname, String your_nickname) throws SQLException;

	public void likeInsert(String my_id, String my_nickname, String your_nickname) throws SQLException;

	// minus
	public void likeMinus(String my_nickname, String your_nickname) throws SQLException;

	public void likeDelete(String my_nickname, String your_nickname) throws SQLException;

	// read
	public List<LikeDto> likeRead(String my_id) throws SQLException;

}

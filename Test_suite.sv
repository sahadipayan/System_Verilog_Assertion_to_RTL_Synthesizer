property 1;
	@(posedge clk) (finished==1'b1) |-> aes_binary.FSM== 3'b110;
endproperty

property 2;
	@(posedge clk) aes_128.key!= aes_128.out;
endproperty

property 3;
		@(posedge clk) disable iff(reset) (empty==1'b1 && read==1'b0) |-> (valid==1'b1 );
endproperty

property 4;
	@(posedge clk) (RSA.FSM == RSA.IDLE) && start|-> (RSA.FSM == RSA.INIT);
endproperty

property 5;
		@(posedge clk) disable iff(reset) (full==1'b1 && read==1'b0) |=> (full==1'b1 );
endproperty

property 6;
		@(posedge clk) disable iff(reset) (full==1'b1 && write==1'b1 && read==1'b0) |=> (full==1'b1 );
endproperty

property 7;
   @(posedge clk)  disable iff (reset) (user_input == 3'b111) || (user_input == 3'b110) |=> (fsm_1.state == 2'h01);
endproperty


property 8;
   @(posedge clk)  disable iff (reset) (user_input == 3'b000) || (user_input == 3'b101) |-> (fsm_1.state == 2'h10);
endproperty


property 9;
	@(posedge clk) ((aes_128.key) ^ (aes_128.state)) |=> aes_128.s0;
endproperty

property 10;
                @(posedge clk) (intialize1^intialize2) |-> cont_1 == 1;
endproperty


property 11;
	@(posedge clk) (finished==1'b1) ##1 (ready==1'b1) |-> aes_binary.FSM== 3'b000;
endproperty

property 12;
		@(posedge clk) disable iff(reset) (full==1'b1 && read==1'b0) ##1 (read == 1'b1) |=> (full==1'b0);

endproperty
class ApiController < ApplicationController
  def create
    @log = Log.new()
    @log.save!
    render json: {isSuccess: true}
  end
  
  def show
    @log = Log.limit(20)
    render json: @log
  end
end

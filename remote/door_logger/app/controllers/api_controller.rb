class ApiController < ApplicationController
  def create
    @log = Log.new()
    @log.save!
    render json: Log.last
  end
  
  def show
    count = params.has_key?(:count) ? params['count'].to_i() : 20
    @log = Log.order(id: "DESC").limit(count)
    render json: @log
  end
end
